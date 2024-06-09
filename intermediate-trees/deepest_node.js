function deepestNode(root) {
  function helper(root) {
    if (!root) {
      return [null, 0];
    }
    if (!root.left && !root.right) {
      return [root.value, 1];
    }
    const [lVal, lDepth] = helper(root.left);
    const [rVal, rDepth] = helper(root.right);
    if (lDepth > rDepth) {
      return [lVal, lDepth + 1];
    } else {
      return [rVal, rDepth + 1];
    }
  }

  const [val, _] = helper(root);
  return val;
}
