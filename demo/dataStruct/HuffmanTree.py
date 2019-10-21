
# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

class HuffmanTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.weight = -1
        self.parent = None
        self.leftChild = None
        self.rightChild = None
    
    def CreateHuffmanTree(self, Nodes):
        TreeNode = Nodes[:]
        
        if len(TreeNode) > 0:
            while len(TreeNode) > 1:
                LeftTreeNode = TreeNode.pop(0)
                RightTreeNode = TreeNode.pop(0)
                NewNode = HuffmanTreeNode()
                NewNode.leftChild = LeftTreeNode
                NewNode.rightChild = RightTreeNode
                NewNode.weight = int(LeftTreeNode.weight) + int(RightTreeNode.weight)
                LeftTreeNode.parent = NewNode
                RightTreeNode.parent = NewNode
                self.InsertTreeNode(TreeNode, NewNode)

            return TreeNode[0]
    
    def InsertTreeNode(self, TreeNode, NewNode):
        if len(TreeNode) > 0:
            tmp = 0
            while tmp < len(TreeNode):
                tWeight = int(TreeNode[tmp].weight)
                if tWeight > NewNode.weight:
                    TreeNode.insert(tmp, NewNode)
                    return
                tmp = tmp + 1
        
        TreeNode.append(NewNode)

    def HuffmanEncoding(self, Root, Nodes, Codes):
        index = range(len(Nodes))
        for item in index:
            temp = Nodes[item]
            tCode = ''
            while temp is not Root:
                if temp.parent.leftChild is temp:
                    tCode = '0' + tCode
                else:
                    tCode = '1' + tCode
                temp = temp.parent
            Codes.append(tCode)
    
    def CreateLeafNodes(self, LeafNodes):
        print('按照叶子结点权值升序，分组输入叶子结点的值和权值，如A 10, 并以# #结束')
        NodeInformation = input('->').split(' ')
        while NodeInformation[1] is not '#':
            NewNode = HuffmanTreeNode()
            NewNode.data = NodeInformation[0]
            NewNode.weight = NodeInformation[1]
            LeafNodes.append(NewNode)
            NodeInformation = input('->').split()

