from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import datetime

class RootApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text=self.calculate_time_difference())
        self.layout.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)  # Update every 1 second
        return self.layout

    def calculate_time_difference(self):
        start_date = datetime.datetime(2022, 9, 1)
        current_date = datetime.datetime.now()
        time_difference = current_date - start_date

        # Extract days, hours, minutes, and seconds from the time difference
        days = time_difference.days
        seconds = time_difference.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        formatted_duration = f"{days} - {hours} - {minutes} - {seconds}"
        return formatted_duration

    def update_time(self, interval):
        self.label.text = self.calculate_time_difference()

if __name__ == "__main__":
    RootApp().run()
