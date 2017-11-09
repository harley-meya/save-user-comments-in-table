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


class GatherText(Component):
    
    def start(self):
        
        # Grab the user's newest comment. flow.value is a builtin variable that
        # stores the user's most recent text.
        new_text = self.db.flow.get("value")
        
        # Get the maximum comment id so we can increment
        comment_id = self.db.table("comments").filter(user_id=self.db.user.id, order_by=["-comment_id"])[0]["comment_id"]
        comment_id += 1
        
        # Add the comment to the comments table
        self.db.table("comments").add({"text": new_text, "comment_id": comment_id, "user_id": self.db.user.id})
        
        # Return to the flow and execute the "next" transition.
        text = "Added {0}".format(self.db.table("comments").filter(user_id=self.db.user.id, order_by=["-comment_id"])[0])
        return self.respond(message=self.create_message(text=text), action="next")