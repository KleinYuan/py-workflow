import uuid
from threading import Thread
from Queue import Queue


class BaseWorker(Thread):
	"""
	Job in job queue should contains following info:
	{
		'id': ,
		'worker': ,
		'data': ,
		'meta': ,

	}
	"""
	def __init__(self, logger, name, job_queue, future_job_queue=Queue(), next_worker=None):
		Thread.__init__(self)
		self.logger = logger
		self.name = name
		self.next_worker = next_worker
		self.job_queue = job_queue
		self.future_job_queue = future_job_queue

	def _deep_log(func):
		def debug_wrapper(*args):
			self = args[0]
			self.logger.debug('[BaseWorker]Executing function {}()'.format(func.__name__))
			func(*args)
			self.logger.debug('[BaseWorker]Executed function {}()'.format(func.__name__))
			self.logger.debug('--------------------------------------')

		return debug_wrapper

	def run(self):
		while True:
			_job = self.job_queue.get()
			assert _job['worker'] == self.name, '[{}] Expecting {}, got {}'.format(self.name, self.name, _job['worker'])
			try:
				_response = self.process(_job)
				self.logger.debug("[ActivityWorker | {}] Processed a job".format(self.name))
			except Exception as e:
				_response = {
					'data': None,
					'meta': None
				}
			_next_job = {
				'id': uuid.uuid4().hex,
				'worker': self.next_worker,
				'data': _response['data'],
				'meta': _response['meta']
			}
			self.job_queue.task_done()
			self.logger.debug("[ActivityWorker | {}] Creating a job to {}".format(self.name, self.next_worker))
			self.future_job_queue.put(_next_job)

	def process(self, job):
		"""
		To be overriden
		:param job:
		:return:
		"""
		response = {
			'data': None,
			'meta': None
		}
		raise NotImplementedError
		return response