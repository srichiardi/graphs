from collections import defaultdict



class EntityCollection(object):
    
    
    def __init__(self):
        ''' Class collecting entities of the same type. '''
        self._entity_reg = {}
        
        
    def addEntity(self, new_entity):
        ''' '''
        self._entity_reg[new_entity.name] = new_entity
    
    
    def getEntity(self, entity_name):
        ''' '''
        return self._entity_reg[entity_name]
    
    
    def getEntities(self):
        ''' Generator returns all entities in the registry'''
    
    
    def removeEntity(self, entity):
        ''' '''
        del self._EntityRegistry[entity.name]
        


class EntityTypes(object):
    
    
    def __init__(self):
        ''' Class storing entities by type. '''
        self._collections = defaultdict(EntityCollection)
        
        
    def addEntity(self, new_entity):
        ''' '''
        self._collections[new_entity.type].addEntity(new_entity)
        
        
    def removeEntity(self, entity):
        ''' '''
        self._collections[entity.type].removeEntity(entity)
    


class Field(object):
    

    def __init__(self):
        ''' The field is the space that holds and manages all other classes. From the field is possible
        to search other create, instances and modify them. '''
        self._entity_reg = EntityTypes() # all entities are kept in this dictionary, searchable by type and name
        
        
    def addLink(self, entity_src, entity_dst):
        ''' Create an undirected edge between two entities '''
        pass
        
        
    def createEntity(self, entity_type, entity_name):
        ''' Create a new entity '''
        new_entity = Entity(entity_type, entity_name, self)
        self._entity_reg.addEntity(new_entity)
        return new_entity
        
        

class Entity(object):
    
    
    def __init__(self, entity_type, entity_name):
        self.type = entity_type
        self.value = entity_name
        self.group = None
        self.links = WeakValueDictionary() # dict of linked entities
    
    
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