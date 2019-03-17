from events.watcher import Watcher


def handler1(previous_state, current_state):
    print('Handler 1 : {} to {}'.format(previous_state, current_state))


def handler2(previous_state, current_state):
    print('Handler 2 : {} to {}'.format(previous_state, current_state))


def handler3(previous_state, current_state):
    print('Handler 3 : {} to {}'.format(previous_state, current_state))
    if current_state == '5':
        file_watcher.stop_watching()


file_path = 'test.txt'


def get_file_contents(_file_path):
    file = open(_file_path, "r")
    return file.read()


file_watcher = Watcher(state_func=get_file_contents, change_handlers=[
                       handler1, handler2, handler3], initial_state=get_file_contents(file_path), state_check_interval=2, _file_path=file_path)

file_watcher.start_watching()
