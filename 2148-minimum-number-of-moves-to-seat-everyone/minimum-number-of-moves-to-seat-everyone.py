class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        m=0
        x=sorted(seats)
        y=sorted(students)
        for i in xrange(len(x)):
                m+=abs(x[i]-y[i])
        return m