#Embedded file name: toontown.coghq.FactoryEntityCreatorAI
from otp.level import EntityCreatorAI
from toontown.toonbase.ToonPythonUtil import Functor
from toontown.coghq import DistributedBeanBarrelAI
from toontown.coghq import DistributedButtonAI
from toontown.coghq import DistributedCrateAI
from toontown.coghq import DistributedLiftAI
from toontown.coghq import DistributedDoorEntityAI
from toontown.coghq import DistributedGagBarrelAI
from toontown.coghq import DistributedGridAI
from toontown.suit import DistributedGridGoonAI
from toontown.suit import DistributedGoonAI
from toontown.coghq import DistributedHealBarrelAI
from toontown.coghq import DistributedStomperPairAI
from toontown.coghq import DistributedTriggerAI
from toontown.coghq import DistributedStomperAI
from toontown.coghq import DistributedLaserFieldAI
from toontown.coghq import DistributedSecurityCameraAI
from toontown.coghq import DistributedMoverAI
from toontown.coghq import DistributedElevatorMarkerAI
from toontown.coghq import DistributedSinkingPlatformAI
from toontown.coghq import ActiveCellAI
from toontown.coghq import CrusherCellAI
from toontown.coghq import DirectionalCellAI
from toontown.coghq import FactoryLevelMgrAI
from toontown.coghq import BattleBlockerAI
from toontown.coghq import DistributedGolfGreenGameAI
from toontown.coghq import DistributedMoleFieldAI
from toontown.coghq import DistributedMazeAI

class FactoryEntityCreatorAI(EntityCreatorAI.EntityCreatorAI):

    def __init__(self, level):
        EntityCreatorAI.EntityCreatorAI.__init__(self, level)
        cDE = EntityCreatorAI.createDistributedEntity
        cLE = EntityCreatorAI.createLocalEntity
        nothing = EntityCreatorAI.nothing
        self.privRegisterTypes({'activeCell': Functor(cDE, ActiveCellAI.ActiveCellAI),
         'crusherCell': Functor(cDE, CrusherCellAI.CrusherCellAI),
         'battleBlocker': Functor(cDE, BattleBlockerAI.BattleBlockerAI),
         'beanBarrel': Functor(cDE, DistributedBeanBarrelAI.DistributedBeanBarrelAI),
         'button': DistributedButtonAI.DistributedButtonAI,
         'conveyorBelt': nothing,
         'crate': Functor(cDE, DistributedCrateAI.DistributedCrateAI),
         'directionalCell': Functor(cDE, DirectionalCellAI.DirectionalCellAI),
         'door': DistributedDoorEntityAI.DistributedDoorEntityAI,
         'gagBarrel': Functor(cDE, DistributedGagBarrelAI.DistributedGagBarrelAI),
         'gear': nothing,
         'goon': Functor(cDE, DistributedGoonAI.DistributedGoonAI),
         'gridGoon': Functor(cDE, DistributedGridGoonAI.DistributedGridGoonAI),
         'golfGreenGame': Functor(cDE, DistributedGolfGreenGameAI.DistributedGolfGreenGameAI),
         'goonClipPlane': nothing,
         'grid': Functor(cDE, DistributedGridAI.DistributedGridAI),
         'healBarrel': Functor(cDE, DistributedHealBarrelAI.DistributedHealBarrelAI),
         'levelMgr': Functor(cLE, FactoryLevelMgrAI.FactoryLevelMgrAI),
         'lift': Functor(cDE, DistributedLiftAI.DistributedLiftAI),
         'mintProduct': nothing,
         'mintProductPallet': nothing,
         'mintShelf': nothing,
         'mover': Functor(cDE, DistributedMoverAI.DistributedMoverAI),
         'paintMixer': nothing,
         'pathMaster': nothing,
         'rendering': nothing,
         'platform': nothing,
         'sinkingPlatform': Functor(cDE, DistributedSinkingPlatformAI.DistributedSinkingPlatformAI),
         'stomper': Functor(cDE, DistributedStomperAI.DistributedStomperAI),
         'stomperPair': Functor(cDE, DistributedStomperPairAI.DistributedStomperPairAI),
         'laserField': Functor(cDE, DistributedLaserFieldAI.DistributedLaserFieldAI),
         'securityCamera': Functor(cDE, DistributedSecurityCameraAI.DistributedSecurityCameraAI),
         'elevatorMarker': Functor(cDE, DistributedElevatorMarkerAI.DistributedElevatorMarkerAI),
         'trigger': DistributedTriggerAI.DistributedTriggerAI,
         'moleField': Functor(cDE, DistributedMoleFieldAI.DistributedMoleFieldAI),
         'maze': Functor(cDE, DistributedMazeAI.DistributedMazeAI)})