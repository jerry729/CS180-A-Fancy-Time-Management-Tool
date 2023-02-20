import random

def test_no_collisions():
    # Create a new schedule with random tasks
    schedule = Schedule()
    schedule.generate_random_tasks()

    # Generate a second set of tasks to place in the schedule
    new_tasks = schedule.generate_random_tasks()

    # Place the new tasks in the schedule using the pre-written function
    schedule.place_tasks(new_tasks)

    # Check that the new tasks have been placed in the schedule correctly
    for task in new_tasks:
        assert task in schedule.tasks

    # Check that there are no time collisions between the tasks
    for task1 in schedule.tasks:
        for task2 in schedule.tasks:
            if task1 != task2:
                assert not task1.time_overlap(task2)

def __init__(self):
    self.tasks = []

def generate_random_tasks(self, n=10):
    for i in range(n):
        # Generate a task with a random start time and duration
        start_time = random.randint(0, 720)
        duration = random.randint(5, 60)
        task = Task(start_time, duration)

        # Add the task to the list of tasks
        self.tasks.append(task)

    return self.tasks