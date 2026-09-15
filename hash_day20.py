# # key   >   value 

# student = {
#     "name " : "Anas",
#     "City" : "Multan",
#     "Semester" : "2nd"
# }

# print(student["Semester"])






Class Queue() {
   private int[100] data;
   int index = -1;

   public int add(int number) {
      
       data.append(number)

       if(data.size() ==1) {
           index = 0;
       }

   }


   public int get() {

       int number = data[index];

       index++;


   }

}


void main() {


Queue q = new Queue();

q.add(5)
q.add(7)
q.add(11)

int number = q.get()
int number = q.get()
int number = q.get()

}