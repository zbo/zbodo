namespace Merge
{
    public class Node
    {
        public int data;
        public Node next;
    } ;

    public class MergeClass
    {
        public Node Merge(Node head1, Node head2)
        {
            if (head1 == null) return head2;
            if (head2 == null) return head1;

            Node resultHead = null;
            if (head1.data <= head2.data)
            {
                resultHead = head1;
                head1 = head1.next;
            }
            else
            {
                resultHead = head2;
                head2 = head2.next;
            }
            Node currentNode = resultHead;
            while (head1 != null && head2 != null)
            {
                if (head1.data <= head2.data)
                {
                    currentNode.next = head1;
                    head1 = head1.next;
                }
                else
                {
                    currentNode.next = head2;
                    head2 = head2.next;
                }
                currentNode = currentNode.next;
            }
            if (head1 != null)
                currentNode.next = head1;
            else
                currentNode.next = head2;

            return resultHead;
        }
    }
}