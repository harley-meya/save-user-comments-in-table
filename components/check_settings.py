# Please read in this order:
#   1. welcome.yaml
#   2. toggle_comment_collection.py
#   3. gather_text.yaml
#   4. gather.py
#   5. gather_complete.yaml
#
from meya import Component


class CheckSettings(Component):
    
    def start(self):
        
        gather = self.db.table("settings").filter(user_id=self.db.user.id)[0]["gather_comments"]
        action = "equal" if gather == True else "notequal"
        
        return self.respond(message=None, action=action)
            