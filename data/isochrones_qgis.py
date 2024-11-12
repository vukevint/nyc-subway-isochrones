v = iface.layerTreeView()
# v.collapseAllNodes()
nodes = v.selectedNodes()
parent = nodes[0].parent()

groups = {}
for n in nodes: 
    key = n.name()[0]
    if not key in groups:
        groups[key]=[]
    groups[key].append(n)

new_groups = {}
for key in groups:
    grp_name = key
    grp = parent.addGroup(grp_name)
    new_groups[key] = grp

for key in groups:
    new_group = new_groups[key]
    for n in groups[key]:
        clone = n.clone()
        new_group.addChildNode(clone)

for key in groups:
    for n in groups[key]:
        parent.removeChildNode(n)