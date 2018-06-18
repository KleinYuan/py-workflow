from lib.base_worker import BaseWorker


class IDAWorker(BaseWorker):

	def process(self, job):
		url = job['data']
		self._mock_download(url)
		response = {
			'data': 'mock data',
			'meta': 'test ida worker'
		}
		return response

	def _mock_download(self, url):
		self.logger.info('Download image from {}'.format(url))
