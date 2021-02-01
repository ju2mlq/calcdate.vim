import pynvim

from datetime import date, timedelta

@pynvim.plugin
class CalcDatePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('CalcDate', nargs='*', range='')
    def calcdate(self, args, range):
        try:
            days = int(args[0])
        except:
            days = 0

        today = date.today()
        target = today - timedelta(days=days)

        self.nvim.feedkeys(f"g,s{target}\n\n")


