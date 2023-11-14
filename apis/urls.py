from rest_framework import routers
from .api import ProjectViewSetMembers, ProjectViewSetUser, ProjectViewSetNovelty, ProjectViewSetPublications, ProjectViewSetRegisterWeek, ProjectViewSetRegisterMicroinverser, ProjectViewSetMaterials
from .views import ProjectViewSetDataMicroinverser

router = routers.DefaultRouter()

router.register("members", ProjectViewSetMembers, "member")
router.register("user", ProjectViewSetUser, "user")
router.register("novelty", ProjectViewSetNovelty, "novelty")
router.register("publications", ProjectViewSetPublications, "publications")
router.register("registerWeek", ProjectViewSetRegisterWeek, "registerWeek")
router.register("registerMicroinverser", ProjectViewSetRegisterMicroinverser, "registerMicroinverser")
router.register("dataMicroinverser", ProjectViewSetDataMicroinverser, "dataMicroinverser")
router.register("materials", ProjectViewSetMaterials, "materials")

urlpatterns = router.urls