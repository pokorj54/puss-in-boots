
import random

class NumberedPictureGatherer:
    def __init__(self, link, max_number, leading_zeros, suffix, emote, trigger_regex):
        assert link[-1] == '/'
        self.link = link
        self.max_number = max_number
        self.leading_zeros = leading_zeros
        self.suffix = suffix
        self.emote = emote
        self.trigger_regex = trigger_regex

    def get(self, match):
        number = random.randrange(1, self.max_number+1)
        return self.link + str(number).zfill(self.leading_zeros) + "." + self.suffix

