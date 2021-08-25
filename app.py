import radio
from excel import Excel

"""
  Check read.me for usage and stuff

  Author:
  Patrik

  Note:
  Use wisely

"""

if __name__ == "__main__":
  excel = Excel()
  controller = radio.RadioScrapping("https://www.radia.sk/radia/fun/playlist", excel)
  # one page contains 50 songs

  months = int(input('Gimme number of months to retrieve data from: '))

  # relocate in months
  controller.relocate(months)

  # page to do scrapping on
  # usualy in one day there are 8 pages of song. It does not matter in 
  # our case so we will not measure this exactly. Maybe I will add function which will run
  # this till the newest titles.
  controller.scraping(months*8*10)

