from image_process_activity_worker import IPAWorker
from image_download_activity_worker import IDAWorker
from lib.base_handler import BaseHandler
import logging


class IPWorkflow(object):

	def __init__(self, job_queue):
		logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s', )
		self.logger = logging

		_handler_name = 'handler'
		_ida_worker_name = 'image_download'
		_ipa_worker_name = 'image_process'
		self.activity_names = [
			_ida_worker_name,
			_ipa_worker_name
		]

		self.handler_name = _handler_name
		self.handler = BaseHandler(
			logger=self.logger,
			name=self.handler_name,
			activity_names=self.activity_names,
			job_queue=job_queue,
			init_worker=_ida_worker_name)

		_activity_queues = self.handler.get_activity_queues()
		_ida_worker_activity_queue = _activity_queues[_ida_worker_name]
		_ipa_worker_activity_queue = _activity_queues[_ipa_worker_name]

		self.ida_worker = IDAWorker(
			logger=self.logger,
			name=_ida_worker_name,
			job_queue=_ida_worker_activity_queue,
			response_queue=_ipa_worker_activity_queue,
			next_worker=_ipa_worker_name)

		self.ipa_worker = IPAWorker(
			logger=self.logger,
			name=_ipa_worker_name,
			job_queue=_ipa_worker_activity_queue)

	def start(self):
		self.handler.start()
		self.ida_worker.start()
		self.ipa_worker.start()


def _test():
	test_workflow = IPWorkflow(job_queue=[])
	test_workflow.start()


if __name__ == '__main__':
	_test()
