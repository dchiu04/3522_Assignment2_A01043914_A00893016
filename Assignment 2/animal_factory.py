import abc

class AnimalFactory(abc.Abc):
    @staticmethod
    def create(stuffing, size, fabric, name, desc, prod_id):
        pass

class SkeletonFactory(AnimalFactory):
    @staticmethod
    def create(glow, **kwargs):
        yarn = "Acrylic Yarn"
        glow_in_dark = glow
        #return Skeleton()