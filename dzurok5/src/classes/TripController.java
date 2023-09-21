package classes;

import interfaces.iCommonInterface;

public class TripController implements iCommonInterface {

	GpsSensor gps;
	private NetController netController;

	public TripController(GpsSensor gps, NetController netController) {
		this.gps = gps;
		this.netController = netController;
	}

	@Override
	public void methodFromInterface() {
		System.out.println("TripController");
	}
}