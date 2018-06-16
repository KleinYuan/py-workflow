# Project

- [X] Single Thread Workflow

- [ ] Multi-Threads Workflow

- [ ] Multi-Processor Workflow

- [ ] Multi-Agent Workflow

- [ ] Python Library


# Run

Do : `python example.py`

You will see:

```
(MainThread) Setting a workflow
(MainThread) [Execution] action1
(MainThread) [ExampleWorkflow] action1
(MainThread) [SetState] action1 completed, setting state to state2
(MainThread) ---------------
(MainThread) [Execution] action2
(MainThread) [ExampleWorkflow] action2
(MainThread) [SetState] action2 completed, setting state to state3
(MainThread) ---------------
(MainThread) [Execution] action3
(MainThread) [ExampleWorkflow] action3
(MainThread) [SetState] action3 completed, setting state to state1
(MainThread) ---------------
(MainThread) [Execution] action1
(MainThread) [ExampleWorkflow] action1
(MainThread) [SetState] action1 completed, setting state to state2
(MainThread) ---------------
(MainThread) [Execution] action2
(MainThread) [ExampleWorkflow] action2
(MainThread) [SetState] action2 completed, setting state to state3

.........
```