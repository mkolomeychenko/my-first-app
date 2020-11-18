import os
import time
import supervisely_lib as sly

my_app = sly.AppService()

task_id = os.environ["TASK_ID"]
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])


@my_app.callback("do_something")
@sly.timeit
def do(api: sly.Api, task_id, context, state, app_logger):
    app_logger.info("do something here")
    # or just print (it is recommended to use app_logger)
    #print("do something here")

    steps_count = 10
    task_progress = sly.Progress("Processing...", steps_count)

    for i in range(steps_count):
        print(i)
        time.sleep(1)

    my_app.stop()


def main():
    sly.logger.info("Input arguments", extra={
        "TASK_ID": task_id,
        "context.teamId": TEAM_ID,
        "context.workspaceId": WORKSPACE_ID
    })

    initial_events = [{"state": None, "context": None, "command": "do_something"}]

    # Run application service
    my_app.run(data=data, state=state, initial_events=initial_events)


if __name__ == "__main__":
    sly.main_wrapper("main", main)