from lib.base_worker import BaseWorker
from Queue import Queue


class BaseDecider(BaseWorker):

	def __init__(self, logger, activity_names, name, job_queue, next_worker):
		self.activity_queues = {}
		self.activity_names = activity_names
		self._initialize_job_queues()
		self._init_job_queue = self.activity_queues[activity_names[0]]
		BaseWorker.__init__(self, logger, name, job_queue, self._init_job_queue, next_worker)

	def _initialize_job_queues(self):
		for name in self.activity_names:
			self.activity_queues[name] = Queue()

	def get_activity_queues(self):
		return self.activity_queues

	def process(self, job):
		self.logger.debug('[Decider] A job (id={}) has been assigned to {}'.format(job['id'], self.next_worker))
		job['worker'] = self.next_worker
		self.activity_queues[self.next_worker].put(job)
		response = {
			'data': job['data'],
			'meta': job['meta']
		}
		return response
