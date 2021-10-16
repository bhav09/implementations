from plyer import notification
import time

def timer(focus_time, short_break, long_break):
    for i in range(4):
        notification.notify(
            title=f'Pomodoro Timer',
            message=f'Great Job! You have focused for {focus_time} mins. straight. Now a take a short break of {short_break} mins.',
            app_icon='pomodoro.ico',timeout=5
        )
        time.sleep(focus_time*60)
        notification.notify(
            title=f'Pomodoro Timer',
            message=f"Fix your lens we are about to get on a focus journey for {focus_time} mins.",
            app_icon='Study.ico',timeout=5
        )
        time.sleep(short_break * 60)
    notification.notify(
        title=f'Pomodoro Timer',
        message=f'Good job! Time to take a good break!\nTotal Focus Time: {4*focus_time} mins\n',
        app_icon='break.ico',timeout=5
    )
    time.sleep(long_break)
timer(25,5,15)