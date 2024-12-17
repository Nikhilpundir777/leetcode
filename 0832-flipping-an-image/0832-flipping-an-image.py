class Solution(object):
    def flipAndInvertImage(self, image):
        self.reverse(image)
        self.invert(image)
        return image

    def reverse(self,image):
        for row in image:
            row.reverse()

    def invert(self,image):
        n=len(image)
        for i in range(n):
            for j in range(n):
                if image[i][j]==0:
                    image[i][j]=1
                elif image[i][j]==1:
                    image[i][j]=0

        