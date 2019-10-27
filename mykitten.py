import time
def main(args):
   pass


def handle_result(args, answer, target_window_id, boss):
    w = boss.window_id_map.get(target_window_id)
    if w is not  None:
#         w.send_text(":wi:")
      # http://jkorpela.fi/chars/c0.html

      # send ctrl-c command
      # if neovim is 0.4.x , use write_to_child and the rest
#       w.write_to_child("\3")
      # if neovim is 0.3.x ,use paste and the rest
      w.paste("\3")

      # need to sleep a little,otherwise it doesn`t work well
      time.sleep(0.005)
      arg= args[1]
      if len(arg)>3 and arg[-2:] =="\\r":
          w.paste(arg[:-2]+"\r")
      elif len(arg)>4 and arg[:4] =="\\x20":
          w.paste("\x20"+arg[4:])
      else:
          w.paste(args[1])


handle_result.no_ui = True
