import logging
import uuid
from threading import Thread
from examples.image_process_workflow import IPWorkflow
import time
from Queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


class Starter(Thread):

	def __init__(self, job_queue):
		Thread.__init__(self)
		self.logger = logging
		self.job_queue = job_queue

	def run(self):
		while True:
			_job = {
				'id': uuid.uuid4().hex,
				'worker': 'decider',
				'data': 'url',
				'meta': 'meta'
			}
			self.job_queue.put(_job)
			self.logger.debug('[Starter] Creating a job ...')
			time.sleep(0.01)


def _test():
	job_queue = Queue()
	test_workflow = IPWorkflow(job_queue=job_queue)
	test_workflow.start()
	test_starter = Starter(job_queue=job_queue)
	test_starter.start()


if __name__ == '__main__':
	_test()
