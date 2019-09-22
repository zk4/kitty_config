import kitty.conf.utils as ku
import kitty.key_encoding as ke
from kitty import keys


def main():
    pass


def actions(extended):
    yield keys.defines.GLFW_PRESS
    if extended:
        yield keys.defines.GLFW_RELEASE


def handle_result(args, result, target_window_id, boss):
    print(args, result, target_window_id,boss)
    print("1")
    w = boss.window_id_map.get(target_window_id)
    tab = boss.active_tab
    if w is None:
        return

    print("2")
#     if w.screen.is_main_linebuf():
#         print("in.....................")
#         getattr(tab, args[1])(args[2])
#         return
#  fix bug for watch command  : watch ls
    getattr(tab, args[1])(args[2])
    return


    print("3")
    mods, key, is_text = ku.parse_kittens_shortcut(args[3])

    if is_text:
        w.send_text(key)
        return

    print("4")
    extended = w.screen.extended_keyboard
    for action in actions(extended):
        sequence = (
            ('\x1b_{}\x1b\\' if extended else '{}')
            .format(
                keys.key_to_bytes(
                    getattr(keys.defines, 'GLFW_KEY_{}'.format(key)),
                    w.screen.cursor_key_mode, extended, mods, action)
                .decode('ascii')))
        print("here...")
        print(sequence)
        w.write_to_child(sequence)


handle_result.no_ui = True
