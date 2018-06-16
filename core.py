import logging
import time
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class WorkFlowManager(object):

    workflow = {}
    state = None
    logger = logging

    def init(self):
        raise NotImplementedError

    def set_workflow(self, workflow):
        self.logger.debug('Setting a workflow')
        self.workflow = workflow

    @classmethod
    def set_activity(*args, **kwargs):
        _end_state = kwargs['end_state']
        def func_wrapper(func):
            def _wrapper(self, *args, **kwargs):
                func(self, *args, **kwargs)
                self.logger.debug('[SetState] {} completed, setting state to {}'.format(func.__name__, _end_state))
                self.state = _end_state
            return _wrapper
        return func_wrapper

    def spin(self):
        self.init()
        while True:
            self.execute()
            time.sleep(2)
            self.logger.debug('---------------')

    def _deep_log(func):
        def debug_wrapper(*args):
            self = args[0]
            self.logger.debug('--------------------------------------')
            self.logger.debug('[DeepLog]Executing function {}()'.format(func.__name__))
            func(*args)
            self.logger.debug('[DeepLog]Executed function {}()'.format(func.__name__))
            self.logger.debug('--------------------------------------')
        return debug_wrapper

    # @_deep_log
    def execute(self):
        _activity_name = self.workflow[self.state]
        self.logger.debug('[Execution] {}'.format(_activity_name))
        activity = getattr(self, _activity_name)
        activity()
