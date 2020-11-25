#!/usr/bin/python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(x1,y1):
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x1
    goal.target_pose.pose.position.y = y1
    goal.target_pose.pose.orientation.w = 1.0
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
x=[10.9,11.25,12.25,12.6,18.2,-2]   #-9.1,-1.2, #
y=[10.55,11,2.0,-1.5,-1.4,4]   #
if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        i=0
        while(i<7):
            result = movebase_client(x[i],y[i]) 
            if result:
                i=i+1
                rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")