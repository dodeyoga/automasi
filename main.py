from trunstop import run_batch_script, press_button, trunstop_close
from jbosstop import activate_window, perform_actions_on_window
from jshell import jshell_batch_script, jshell_button, close_jshell
from jbosstart import jboss_batch_script, jboss_button
from trunstart import trun_start, trun_actions, trunstart_close
from web import web_start
import time

def main():
    
    #Process Stop
    batch_script_path = r'E:\Temenos\BSGPROD\tRun.bat'
    run_batch_script(batch_script_path)
    press_button()
    time.sleep(5)
    trunstop_close('tafj.properties')

    window_name = "Administrator:  JBoss BSGPROD"
    activated_window = activate_window(window_name)
    perform_actions_on_window(activated_window)
    
    jshell_batch_path = r'E:\Temenos\BSGPROD\jShel.bat'
    jshell_batch_script(jshell_batch_path)
    jshell_button()
    time.sleep(5)
    close_jshell('Database Operations')
    
    #Process Start
    jboss_script_path = r'E:\Temenos\BSGPROD\jBossBSGPROD.bat'
    jboss_batch_script(jboss_script_path)
    jboss_button()
    
    start_script_path = r'E:\Temenos\BSGPROD\tRun.bat'
    trun_start(start_script_path)
    trun_actions()
    time.sleep(5)
    trunstart_close('tafj.properties')
    
    web_start()

if __name__ == "__main__":
    main()