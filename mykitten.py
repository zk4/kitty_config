import time
def main(args):
   pass


def handle_result(args, answer, target_window_id, boss):
#   get the kitty window into which to paste answer
    w = boss.window_id_map.get(target_window_id)
    if w is not  None:
#         w.send_text(":wi:")
      # http://jkorpela.fi/chars/c0.html
      # send ctrl-c command
      w.write_to_child("\3")
      # need to sleep a little,otherwise it doesn`t work well
      time.sleep(0.005)
      arg= args[1]
      if len(arg)>3 and arg[-2:] =="\\r":
          w.write_to_child(arg[:-2]+"\r")
      elif len(arg)>4 and arg[:4] =="\\x20":
          w.write_to_child("\x20"+arg[4:])
      else:
          w.write_to_child(args[1])


handle_result.no_ui = True
