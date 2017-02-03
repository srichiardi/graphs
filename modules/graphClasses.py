from collections import defaultdict


class EntityCollection(object):
    
    
    def __init__(self):
        ''' Class collecting entities of the same type. '''
        self._EntityRegistry = {}
        
        
    def addEntity(self, new_entity):
        ''' '''
        self._EntityRegistry[new_entity.name] = new_entity
    
    
    def getEntity(self, entity_name):
        ''' '''
        pass
    
    
    def removeEntity(self, entity_name):
        


class EntityTypes(object):
    
    
    def __init__(self):
        ''' Helper class to store entities by type. '''
        self._collections = defaultdict(EntityCollection)
        
        
    def addEntity(self, new_type, new_entity):
        ''' '''
        self._collections[new_type].addEntity(new_entity)
    


class Field(object):
    

    def __init__(self):
        ''' The field is the space that holds and manages all other classes. From the field is possible
        to search other create, instances and modify them. '''
        self._entityRegistry = {} # all entities are kept in this dictionary, searchable by type and name
        
        
    def getEntity(self, eType, eValue):
        ''' Lookup en existing entity '''
        pass
        
        
    def createEntity(self, eType, eValue):
        ''' Create a new entity '''
        newEntity = Entity(eType, eValue, self)
        return newEntity
        
        

class Entity(object):
    
    
    def __init__(self, entType, entValue, entField):
        if isinstance(entField, Field):
            self.type = entType
            self.value = entValue
            self.field = entField
            self.group = None
            self.links = WeakValueDictionary() # dict of linked entities
            self.field.registerEntity(self) # update the entity registry
        else:
            raise TypeError("Invalid field argument, field instance expected!")
    
    
    def linkTo(self, eTwo):
        ''' Linking operation is bi-directional, affects both entities equally.'''
        pass
    
    
    def getLinks(self):
        ''' Print the list of entities directly linked.'''
        pass
    
    
    def removeLink(self, eTwo):
        ''' Remove linked entity.'''
        pass
    
    
    def __repr__(self):
        return repr(self.value)
    
    
    def __del__(self):
        ''' Delete itself from linked entities, and delete links.'''
        # remove link from linked entity necessary? no because it's a weaklink
        for linkId in self.links.keys():
            self.field.eliminateEdge(linkId)
            
        del self