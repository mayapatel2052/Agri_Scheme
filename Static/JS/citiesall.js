var district_arr = new Array("All","Ahmedabad","Amreli","Anand","Aravalli","Banaskantha (Palanpur)","Bharuch","Bhavnagar","Botad","Chhota Udepur","Dahod","Dangs (Ahwa)","Devbhoomi Dwarka","Gandhinagar","Gir Somnath","Jamnagar","Junagadh","Kachchh","Kheda","Mahisagar","Mehsana","Morbi","Narmada (Rajpipla)","Navsari","Panchmahal (Godhra)","Patan","Porbandar","Rajkot","Sabarkantha (Himmatnagar)","Surat","Surendranagar","Tapi (Vyara)","Vadodara","Valsad");

var d_t = new Array();
d_t[0]="";
d_t[1]=" All ";
d_t[2]=" All | City East | City West | Bavla | Daskroi | Detroj-Rampura | Dhandhuka | Dholera | Dholka | Mandal | Sanand | Viramgam ";
d_t[3]=" All | Amreli | Babra | Bagasara | Dhari | Jafrabad | Khambha | Kunkavav | vadia | Lathi | Lilia | Rajula | Savarkundla ";
d_t[4]=" All | Anand | Anklav | Borsad | Khambhat | Petlad | Sojitra | Tarapur | Umreth ";
d_t[5]=" All | Bayad | Bhiloda | Dhansura | Malpur | Meghraj | Modasa ";
d_t[6]=" All | Amirgadh | Bhabhar | Danta | Dantiwada | Deesa | Deodar | Dhanera | Kankrej | Lakhani | Palanpur | Suigam | Tharad | Vadgam | Vav ";
d_t[7]=" All | Bharuch | Amod | Ankleshwar | Hansot | Jambusar | Jhagadia | Netrang | Vagra | Valia ";
d_t[8]=" All | Bhavnagar | Gariadhar | Ghogha | Jesar | Mahuva | Palitana | Sihor | Talaja | Umrala | Vallabhipur ";
d_t[9]=" All | Botad | Barwala | Gadhada | Ranpur ";
d_t[10]=" All | Chhota Udepur | Bodeli | Jetpur pavi | Kavant | Nasvadi | Sankheda ";
d_t[11]=" All | Dahod | Devgadh baria | Dhanpur | Fatepura | Garbada | Limkheda | Sanjeli | Jhalod ";
d_t[12]=" All | Ahwa | Subir | Waghai ";
d_t[13]=" All | Bhanvad | Kalyanpur | Khambhalia | Okhamandal ";
d_t[14]=" All | Gandhinagar |Dehgam |Kalol |Mansa ";
d_t[15]=" All | Gir Gadhda | Kodinar | Veraval | Sutrapada | Talala | Una ";
d_t[16]=" All | Jamnagar | Dhrol | Jamjodhpur | Jodiya | Kalavad | Lalpur ";
d_t[17]=" All | Junagadh taluka | Bhesana | Junagadh Rural | Keshod | Malia | Manavadar | Mangrol | Mendarda | Vanthali | Visavadar ";
d_t[18]=" All | Abdasa | Anjar | Bhachau | Bhuj | Gandhidham | Lakhpat | Mandvi | Mundra | Nakhatrana | Rapar ";
d_t[19]=" All | Kheda | Galteshwar | Kapadvanj | Kathlal | Mahudha | Matar | Mehmedabad | Nadiad | Thasra | Vaso ";
d_t[20]=" All | Balasinor | Kadana | Khanpur | Lunawada | Santrampur | Virpur ";
d_t[21]=" All | Mehsana | Becharaji | Jotana | Kadi | Kheralu | Satlasana | Unjha | Vadnagar | Vijapur | Visnagar ";
d_t[22]=" All | Halvad | Maliya | Morbi | Tankara | Wankaner ";
d_t[23]=" All | Dediapada | Garudeshwar | Nandod | Sagbara | Tilakwada ";
d_t[24]=" All | Navsari | Vansda | Chikhli | Gandevi | Jalalpore | Khergam ";
d_t[25]=" All | Ghoghamba | Godhra | Halol | Jambughoda | Kalol | Morwa Hadaf | Shehera ";
d_t[26]=" All | Patan | Chanasma | Harij | Radhanpur | Sami | Sankheswar | Santalpur | Sarasvati | Sidhpur ";
d_t[27]=" All | Porbandar | Kutiyana | Ranavav ";
d_t[28]=" All | Rajkot | Dhoraji | Gondal | Jamkandorna | Jasdan | Jetpur | Kotada Sangani | Lodhika | Paddhari | Upleta | Vinchchiya ";
d_t[29]=" All | Himatnagar | Idar | Khedbrahma | Poshina | Prantij | Talod | Vadali | Vijaynagar ";
d_t[30]=" All | Surat | Bardoli | Choryasi | Kamrej | Mahuva | Mandvi | Mangrol | Olpad | Palsana | Umarpada ";
d_t[31]=" All | Chotila | Chuda | Dasada | Dhrangadhra | Lakhtar | Limbdi | Muli | Sayla | Thangadh | Wadhwan ";
d_t[32]=" All | Nizar | Songadh | Uchchhal | Valod | Vyara | Kukurmunda ";
d_t[33]=" All | Vadodara | Dabhoi | Desar | Karjan | Padra | Savli | Sinor | Vaghodia ";
d_t[34]=" All | Valsad | Dharampur | Kaprada | Pardi | Umbergaon | Vapi ";

function print_district(district_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(district_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select district','');
	option_str.selectedIndex = 0;
	for (var i=0; i<district_arr.length; i++) {
		option_str.options[option_str.length] = new Option(district_arr[i],district_arr[i]);
	}
}


function print_taluka(taluka_id, taluka_index){
	var option_str = document.getElementById(taluka_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select taluka','');
	option_str.selectedIndex = 0;
	var taluka_arr = d_t[taluka_index].split("|");
	for (var i=0; i<taluka_arr.length; i++) {
		option_str.options[option_str.length] = new Option(taluka_arr[i],taluka_arr[i]);
	}
}
