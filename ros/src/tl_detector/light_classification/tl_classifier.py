from styx_msgs.msg import TrafficLight
import rospy

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        #pass
	
	rospy.loginfo("Init TLClassfier !")
	self.count = 0

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
	
	self.count += 1        
	
	#rospy.logwarn("The tl_count is %d",self.count)

	if self.count > 200 :
	
	    if (self.count > 210):
	        self.count = 0
	    
	    rospy.logwarn(" TrafficLight is RED")

	
	    return TrafficLight.RED

		
	return TrafficLight.UNKNOWN
