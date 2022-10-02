#include <iostream>
#include <fstream>

using namespace std;

class Vehicle {
    protected:
    unsigned int capacity,mileage,id;
    string vname,vtype,cname;
    
    public:
    void gatherData(){
        cout << "Name of the Vehicle: ";
        cin >> vname;
        cout << "\nType of the Vehicle: ";
        cin >> vtype;
        cout << "\nCompany Name of the Vehicle: ";
        cin >> cname;
        cout << "\nCapacity of the Vehicle(in cc): ";
        cin >> capacity;
        cout << "\nMileage of the Vehicle (in Kmpl): ";
        cin >> mileage; 
        id++;
    }

    void displayData(){
        fstream file;
	cout << "\nAll Vehicles";
	file.open("vehicle.txt", ios::in);
	if (!file)
		cout << "\n\nFile Opening Error!";
	else {

		cout << "\n\n\nV_ID\tName"
			<< "\tCompany\tType" << 
				"\tCapacity\tMileage\n\n";
		file >> id >> vname;
		file >> cname >> vtype;
        file >> capacity >> mileage;
		while (!file.eof()) {
			cout << " " << id
				<< "\t" << vname
				<< "\t" << cname
				<< "\t" << vtype
                << "\t" << capacity
				<< "\t\t" << mileage
				<< "\n\n";
        file >> id >> vname;
		file >> cname >> vtype;
        file >> capacity >> mileage;
		
		}
		file.close();
	}

    }

    void write(){
        ofstream write;
        write.open("vehicle.txt",ios::app);
        if (!write){
            cout << "\nFile could not be found or File could not be created.";
        }else {
        cout << "\nWriting Data to File...\n";
         write << id << " " << vname << " " << cname << " " << vtype << " " << capacity << " " << mileage << " " << "Abhishek" << endl;
        write.close();
        cout << "Data has been exported to file named vehicle.txt";
        }
    
        
    }
    void updateData() {
        unsigned int capacity_c,mileage_c,vid,flag=0,choice;
        string vname_c,vtype_c,cname_c;
        ofstream write;
        ifstream read;
        cout << "\n\nUpdate Vehicle Record";
        write.open("temp.txt", ios::app);
        read.open("vehicle.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            cout << "\nVehicle ID: ";
            cin >> vid;
                read >> id;
                read >> vname;
                read >> cname;
                read >> vtype;
                read >> capacity;
                read >> mileage;
            
            while (!read.eof()){
                if(vid != id){
                    write << id << " " << vname << " " << cname << " " << vtype << " " << capacity << " " << mileage << endl;
                } else {
	            cout << "\nVehicle Name           ----->(1)";
                cout << "\nVehicle Company Name   ----->(2)";
                cout << "\nVehicle Type           ----->(3)";
                cout << "\nCapacity               ----->(4)";
                cout << "\nMileage                ----->(5)";
                cout << "\nWhat would you like to modify? ";
                cin >> choice;
                if(choice==1){
                    cout << "\nEnter New Vehicle Name: ";
                    cin >> vname_c;
                    write << id << " " << vname_c << " " << cname << " " << vtype << " " << capacity << " " << mileage << endl;

                } else if(choice==2){
                    cout << "\nEnter New Vehicle Company Name: ";
                    cin >> cname_c;
                    write << id << " " << vname << " " << cname_c << " " << vtype << " " << capacity << " " << mileage << endl;

                } else if(choice==3){
                    cout << "\nEnter New Vehicle Type: ";
                    cin >> vtype_c;
                    write << id << " " << vname << " " << cname << " " << vtype_c << " " << capacity << " " << mileage << endl;

                } else if(choice==4){
                    cout << "\nEnter New Vehicle Capacity: ";
                    cin >> capacity_c;
                    write << id << " " << vname << " " << cname << " " << vtype << " " << capacity_c << " " << mileage << endl;

                } else if(choice==5){
                    cout << "\nEnter New Vehicle Mileage: ";
                    cin >> vname_c;
                    write << id << " " << vname << " " << cname << " " << vtype << " " << capacity << " " << mileage_c << endl;

                } else {
                    cout << "\nInvalid Input. Please Try Again.";
                }
                flag++;
                } 
                read >> id;
                read >> vname;
                read >> cname;
                read >> vtype;
                read >> capacity;
                read >> mileage;
            }
            if(flag==0){
                    cout << "\nVehicle ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("vehicle.txt");
        rename("temp.txt", "vehicle.txt");


    }
    void deleteData() {
    fstream file, file1;
    int found = 0;
    int VNum;
    cout << "\nDelete Vehicle Details." << endl;

    file.open("vehicle.txt", ios::in);
    if (!file)
    {
        cout << "\nFile Not Found.";
        file.close();
    }
    else
    {
        cout << "\nVehicle ID:  ";
        cin >> VNum;
        file1.open("temp.txt", ios::app | ios::out);
        file >> id >> vname >> cname >> vtype >> capacity >> mileage;
        while (!file.eof())
        {
            if (VNum != id)
            {
                file1 << " " << id << " " << vname << " " << cname<< " " << vtype << " " << capacity << " " << mileage << "\n";
            }
            else
            {
                found++;
                cout << "\nVehicle Data has been deleted successfully.";
            }
            file >> id >> vname >> cname >> vtype >> capacity >> mileage;
        }
        if (found == 0)
        {
            cout << "\nVehicle ID not found.";
        }
        file1.close();
        file.close();
        remove("vehicle.txt");
        rename("temp.txt", "vehicle.txt");
    }
}

};

int main(){
    Vehicle execute;
    int loop = 0,a;
    while (loop == 0){
        cout << "\n=-=-=-=-=-=TSDL Vehicle Database=-=-=-=-=-=";
        cout << "\nAdd Data    ----->(1)";
        cout << "\nView Data   ----->(2)";
        cout << "\nModify Data ----->(3)";
        cout << "\nDelete Data ----->(4)";
        cout << "\nExit        ----->(0)";
        cout << "\nWhat would you like to do?: ";
        cin >> a;

        if(a==1){
            execute.gatherData();
            execute.write();
        } else if(a==2){
            execute.displayData();
        } else if (a==3){
            execute.updateData();
        } else if (a==4){
            execute.deleteData();
        } else if(a==0) {
            break;
        } else {
            cout << "\nInvalid Choice. Please Try again.";
        }

    }
}

