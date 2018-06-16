from core import WorkFlowManager


class ExampleWorkflow(WorkFlowManager):

    def init(self):
        self.state = 'state1'
        workflow = {
            'state1': 'action1',
            'state2': 'action2',
            'state3': 'action3'
        }
        self.set_workflow(workflow=workflow)

    @WorkFlowManager.set_activity(end_state='state2')
    def action1(self):
        self.logger.debug('[ExampleWorkflow] action1')

    @WorkFlowManager.set_activity(end_state='state3')
    def action2(self):
        self.logger.debug('[ExampleWorkflow] action2')

    @WorkFlowManager.set_activity(end_state='state1')
    def action3(self):
        self.logger.debug('[ExampleWorkflow] action3')


test = ExampleWorkflow()
test.spin()
