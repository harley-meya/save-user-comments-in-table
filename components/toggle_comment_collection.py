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


class UpdateSettings(Component):
    
    def start(self):
        
        # First, check to see if this user is in the table. filter returns a
        # list, so if it's length is greater than 0, our user has a record.
        if len(self.db.table("settings").filter(user_id__contains=self.db.user.id)) > 0:
            
            # Now check the setting.
            setting = self.db.table("settings").filter(user_id=self.db.user.id)[0]
            
            if setting["gather_comments"] == False:
            
                # First, create a table to hold our settings and the user's
                # comments. Keep in mind this table is shared between all users,
                # so we have to track each user's id.
                setting.update({"gather_comments": True, "user_id": self.db.user.id})
                self.db.table("comments").add({"text": "", "comment_id": 0, "user_id": self.db.user.id})
                
            else:

                # Turn off comment collection
                self.db.table("settings").update(setting["id"], {"gather_comments": False, "user_id": self.db.user.id})
                
                # Delete all their comments
                comments = self.db.table("comments").filter(user_id=self.db.user.id)
                for comment in comments:
                    self.db.table("comments").delete(comment)
        
        # If the user is not in the table       
        else:
            self.db.table("settings").add({"gather_comments": True, "user_id": self.db.user.id})
            self.db.table("comments").add({"text": "", "comment_id": 0, "user_id": self.db.user.id})

        # Return to the flow that called this component.
        return self.respond(message=None, action="next")