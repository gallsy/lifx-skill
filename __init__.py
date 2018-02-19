# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from lifxlan import BLUE, GREEN, LifxLAN
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'gallsy'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class LifxControlSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(LifxControlSkill, self).__init__(name="LifxControlSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        lights_on_intent = IntentBuilder("LightsOnIntent").\
            require("LightsOnKeyword").build()
        self.register_intent(lights_on_intent, self.handle_lights_on_intent)

        lights_off_intent = IntentBuilder("LightsOffIntent").\
            require("LightsOffKeyword").build()
        self.register_intent(lights_off_intent,
                             self.handle_lights_off_intent)

        lights_dim_intent = IntentBuilder("LightsDimIntent").\
            require("LightsDimeyword").build()
        self.register_intent(lights_dim_intent,
                             self.handle_lights_dim_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_lights_on_intent(self, message):
        self.speak_dialog("light.on")
        lifx = LifxLAN()
        
        for light in lifx.get_lights():
            if light.get_label() == "Gallsy's Light Emporium":
                bulb = light
        
        light.set_power("on")

    def handle_lights_off_intent(self, message):
        self.speak_dialog("light.off")
        lifx = LifxLAN()
        
        for light in lifx.get_lights():
            if light.get_label() == "Gallsy's Light Emporium":
                bulb = light
        
        light.set_power("off")

    def handle_lights_dim_intent(self, message):
        self.speak_dialog("light.dim")
    
    def handle_lights_bright_intent(self, message):
        self.speak_dialog("light.bright")
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LifxControlSkill()
