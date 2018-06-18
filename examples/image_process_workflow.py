from image_process_activity_worker import IPAWorker
from image_download_activity_worker import IDAWorker
from lib.base_decider import BaseDecider
import logging


class IPWorkflow(object):

	def __init__(self, job_queue):
		logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s', )
		self.logger = logging
		self.activity_names = [
			'image_download',
			'image_process'
		]

		self.decider_name = 'decider'
		self.decider = BaseDecider(
			logger=self.logger,
			name=self.decider_name,
			activity_names=self.activity_names,
			job_queue=job_queue,
			next_worker='image_download')

		_activity_queues = self.decider.get_activity_queues()
		self.ida_worker = IDAWorker(
			logger=self.logger,
			name='image_download',
			job_queue=_activity_queues['image_download'],
			future_job_queue=_activity_queues['image_process'],
			next_worker='image_process')

		self.ipa_worker = IPAWorker(
			logger=self.logger,
			name='image_process',
			job_queue=_activity_queues['image_process'])

	def start(self):
		self.decider.start()
		self.ida_worker.start()
		self.ipa_worker.start()


def _test():
	test_workflow = IPWorkflow(job_queue=[])
	test_workflow.start()


if __name__ == '__main__':
	_test()
