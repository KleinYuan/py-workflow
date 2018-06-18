from lib.base_worker import BaseWorker


class IPAWorker(BaseWorker):

	def process(self, job):
		_img = job['data']
		self._mock_up_process_image(_img)
		response = {
			'data': 'mock data',
			'meta': 'test ida worker'
		}
		return response

	def _mock_up_process_image(self, img):
		self.logger.info('Process image ...')
