# Please read in this order:
#   1. welcome.yaml
#   2. toggle_comment_collection.py
#   3. gather_text.yaml
#   4. check_settings.py
#   5. gather.py
#   6. gather_complete.yaml
#   7. display_comments.py
#
from meya import Component


class CheckSettings(Component):
    
    def start(self):
        
        gather = self.db.table("settings").filter(user_id=self.db.user.id)[0]["gather_comments"]
        action = "equal" if gather == True else "notequal"
        
        return self.respond(message=None, action=action)
            