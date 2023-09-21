package classes;

import interfaces.iCityObjectRepository;
import interfaces.iCommonInterface;

public class MapController implements iCommonInterface {

	private iCityObjectRepository cityObjectRepository;
	private TripController tripController;

	public MapController(iCityObjectRepository cityObjectRepository, TripController tripController) {
		this.cityObjectRepository = cityObjectRepository;
		this.tripController = tripController;
	}

	@Override
	public void methodFromInterface() {
		System.out.println("MapController");
	}
}