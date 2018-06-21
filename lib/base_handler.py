from threading import Thread
from Queue import Queue


class BaseHandler(Thread):

	def __init__(self, logger, activity_names, name, job_queue, init_worker):
		Thread.__init__(self)
		self.activity_queues = {}
		self.activity_names = activity_names
		self._initialize_job_queues()
		self._init_job_queue = self.activity_queues[activity_names[0]]
		self.init_worker = init_worker
		self.logger = logger
		self.name = name
		self.job_queue = job_queue

	def _initialize_job_queues(self):
		for name in self.activity_names:
			self.activity_queues[name] = Queue()

	def get_activity_queues(self):
		return self.activity_queues

	def run(self):
		while True:
			_job = self.job_queue.get()
			assert _job['worker'] == self.name, '[{}] Expecting {}, got {}'.format(self.name, self.name, _job['worker'])
			try:
				self._deliver_job(_job)
				self.logger.debug("[Handler | {}] Processed a job".format(self.name))
			except Exception as e:
				self.logger.debug("[Handler | {}] Error: \n{}".format(self.name, e))
			self.job_queue.task_done()

	def _deliver_job(self, job):
		self.logger.debug('[Handler] A job (id={}) has been assigned to {}'.format(job['id'], self.init_worker))
		job['worker'] = self.init_worker
		self.activity_queues[self.init_worker].put(job)
