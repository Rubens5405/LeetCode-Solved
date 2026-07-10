class Solution(object):
    def reverseList(self, head):
        anterior = None
        atual = head
        while atual is not None:
            novo_no = atual.next
            atual.next = anterior
            anterior = atual
            atual = novo_no 
        return anterior  