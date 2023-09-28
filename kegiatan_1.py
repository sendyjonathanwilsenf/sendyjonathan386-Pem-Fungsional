class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_tree(root):
    if root is None:
        return 0

    if root.value == '+':
        return evaluate_tree(root.left) + evaluate_tree(root.right)
    elif root.value == '-':
        return evaluate_tree(root.left) - evaluate_tree(root.right)
    elif root.value == '*':
        return evaluate_tree(root.left) * evaluate_tree(root.right)
    elif root.value == '/':
        return evaluate_tree(root.left) / evaluate_tree(root.right)
    else:
        return float(root.value)  # jika node adalah angka

# Buat pohon aritmatika dengan contoh ekspresi: (3 + 4) * (5 - 2)
root = TreeNode('*')
root.left = TreeNode('+')
root.right = TreeNode('-')
root.left.left = TreeNode('3')
root.left.right = TreeNode('4')
root.right.left = TreeNode('5')
root.right.right = TreeNode('2')

# Evaluasi pohon aritmatika
hasil = evaluate_tree(root)
print("Hasil evaluasi ekspresi (3 + 4) * (5 - 2) adalah:", hasil)