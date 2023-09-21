package classes;

import interfaces.iCommonInterface;
import interfaces.iGUI;
import interfaces.iUxControllers;

public class AppController implements iCommonInterface {
	private iGUI myGui;
	private iUxControllers myIUxControllers;

	private MapController mapController;

	public AppController(iGUI myGui, iUxControllers myIUxControllers, MapController mapController) {
		this.myGui = myGui;
		this.myIUxControllers = myIUxControllers;
		this.mapController = mapController;
	}

	@Override
	public void methodFromInterface() {
		System.out.println("AppController");
	}
}