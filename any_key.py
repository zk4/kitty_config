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

    if w.screen.is_main_linebuf():
        getattr(tab, args[1])(args[2])
        return

    mods, key, is_text = ku.parse_kittens_shortcut(args[3])

    if is_text:
        w.send_text(key)
        return

    

handle_result.no_ui = True
