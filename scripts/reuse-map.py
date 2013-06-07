
import re

claimed = [
	"(.*) claimed",
	"claimed (.+)", 
	"(.*) taken", 
	"(.*) gone", 
	"took (.+)"
]
not_claimed = [
	"(.+) not claimed", 
	"(.+) still there", 
	"(.+) remain", 
	"(.+) remains", 
	"(.+) not taken"
]
quantity = [
	"both", 
	"all", 
	"one", 
	"a few"
]
bldg = "([new]*\d\d?[newabcp])"
room = bldg+"-[a-z]?\d\d\d?\d?"
places = [
	"("+bldg+" loading dock)", 
	"(lobby \d+)", 
	"(room "+room+")", 
	"(outside (?:of)? "+room+")", 
	"(\w+ floor (?:of)? b(?:ui)?ld(?:in)?g? "+bldg+")",
	"(b(?:ui)?ld(?:in)?g? "+bldg+",? floor \w+)",
	"(b(?:ui)?ld(?:in?)g? "+bldg+",? \w+ floor)",
	"(.+ floor .+ .+)",
	"("+room+")", 
	"(b(?:ui)?ld(?:in)?g? "+bldg+")"
]