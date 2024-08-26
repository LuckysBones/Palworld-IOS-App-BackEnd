#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <thread>

int main(){

	//Starts Server
	system("sudo systemctl start palserver");

	while (true) {
       		// Get the current time, using chorno
	        auto now = std::chrono::system_clock::now();
        	auto now_time = std::chrono::system_clock::to_time_t(now);
        	struct std::tm *parts = std::localtime(&now_time);

        	// If statement checks for time of day, if its 02:30 or 14:30
        	if ((parts->tm_hour == 14 || parts->tm_hour == 02) && parts->tm_min == 30) {
			//Start Server Restart Timer
                        system("./palplayers.sh");
			//Continue Server Restart Timer
                        system("./restart-2.sh");

           		// Stop Server
			system("sudo systemctl stop palserver");

			// Start Server
                        system("sudo systemctl start palserver");
        	}

        	// Sleep for some time before checking/restarting again
        	std::this_thread::sleep_for(std::chrono::seconds(30));
    	}

	return 0;
}

