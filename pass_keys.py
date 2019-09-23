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
    w = boss.window_id_map.get(target_window_id)
    tab = boss.active_tab
    if w is None:
        return
    if w.screen.is_main_linebuf() or (w.screen.is_using_alternate_linebuf() and not w.title.strip().startswith("nvim")):
        getattr(tab, args[1])(args[2])
        return

    print("2---------------------------------------------")
    # vim and kitty interactive move
    mods, key, is_text = ku.parse_kittens_shortcut(args[3])
    print(keys)
    print(modes)
    print(is_text)
    if is_text:
        w.send_text(key)
        return

#     print("3---------------------------------------------")
#     extended = w.screen.extended_keyboard
#     for action in actions(extended):
#         sequence = (
#             ('\x1b_{}\x1b\\' if extended else '{}')
#             .format(
#                 keys.key_to_bytes(
#                     getattr(keys.defines, 'GLFW_KEY_{}'.format(key)),
#                     w.screen.cursor_key_mode, extended, mods, action)
#                 .decode('ascii')))
#         w.write_to_child(sequence)


handle_result.no_ui = True
