import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, Image, View } from 'react-native';
export default function App() {
  return (
    <View style={styles.backgroundParent}>
      <View style={[styles.background1, styles.statsBoxPosition]} />
      <View style={styles.mainFrame} />
      <Image style={styles.menuIcon} resizeMode="cover" source="menu.png" />
      <View style={[styles.menuIcon, styles.boxBg]} />
      <Image style={styles.addButtonIcon1} resizeMode="cover" source={require('./assets/add-button.png')} />
      <View style={[styles.achievements1, styles.boxBg]} />
      <View style={[styles.avatarBox, styles.statsLayout]} />
      <Image source={require('./assets/avatar.png')}style={styles.avatarIcon} resizeMode="cover"  />
      <View style={[styles.stats, styles.statsLayout]}>
        <View style={[styles.statsBox, styles.statsLayout]} />
        <View style={[styles.incomeBox, styles.boxShadowBox]} />
        <View style={[styles.familyBox, styles.boxShadowBox]} />
        <View style={[styles.hobbiesBox, styles.boxShadowBox]} />
        <View style={[styles.friendBox, styles.boxShadowBox]} />
        <View style={[styles.healthBox, styles.boxShadowBox]} />
        <Text style={[styles.family, styles.StatString]}>Family</Text>
        <Text style={[styles.health, styles.StatString]}>Health</Text>
        <Text style={[styles.friendship, styles.StatString]}>Friendship</Text>
        <Text style={[styles.hobbies, styles.StatString]}>Hobbies</Text>
        <Text style={[styles.income, styles.StatString]}>Income/Education</Text>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  statsBoxPosition: {
    left: 0,
    top: 0
    },
    boxBg: {
    backgroundColor: "#984fa1",
    borderRadius: 5,
    opacity: 0.8
    },
    statsLayout: {
    height: 150,
    width: 99,
    position: "absolute"
    },
    boxShadowBox: {
    height: 15,
    width: 78,
    borderColor: "rgba(250, 171, 174, 0.68)",
    backgroundColor: "#faabae",
    left: 11,
    borderWidth: 1,
    borderStyle: "solid",
    shadowOpacity: 1,
    elevation: 4,
    shadowRadius: 4,
    shadowOffset: {
    width: 0,
    height: 4
    },
    shadowColor: "rgba(0, 0, 0, 0.25)",
    position: "absolute"
    },
    barIconPosition1: {
    height: 12,
    left: 13,
    position: "absolute"
    },
    barIconPosition: {
    left: 12,
    height: 12,
    position: "absolute"
    },
    StatString: {
    left: 14,
    height: 9,
    textAlign: "left",
    color: "#fff",
    fontFamily: "Inter-Regular",
    fontSize: 7,
    position: "absolute"
    },
    background1: {
    backgroundColor: "#9764af",
    width: 279,
    position: "absolute",
    height: 461
    },
    mainFrame: {
    top: 13,
    left: 20,
    borderRadius: 13,
    backgroundColor: "#712aa0",
    borderColor: "#712aa0",
    width: 246,
    height: 435,
    borderWidth: 1,
    borderStyle: "solid",
    shadowOpacity: 1,
    elevation: 4,
    shadowRadius: 4,
    shadowOffset: {
    width: 0,
    height: 4
    },
    shadowColor: "rgba(0, 0, 0, 0.25)",
    position: "absolute"
    },
    achievements1: {
    top: 195,
    width: 208,
    height: 54,
    opacity: 0.8,
    left: 45,
    borderRadius: 5,
    position: "absolute"
    },
    menuIcon: {
    top: 388,
    left: 45,
    borderRadius: 10,
    width: 208,
    height: 54,
    opacity: 0.8,
    position: "absolute"
    },
    addButtonIcon1: {
    top: 399,
    left: 123,
    height: 29,
    width: 33,
    position: "absolute"
    },
    avatarBox: {
    top: 31,
    width: 99,
    opacity: 0.8,
    backgroundColor: "#984fa1",
    borderRadius: 5,
    left: 45
    },
    avatarIcon: {
    top: 47,
    left: 61,
    width: 67,
    height: 119,
    position: "absolute"
    },
    statsBox: {
    opacity: 0.8,
    backgroundColor: "#984fa1",
    borderRadius: 5,
    left: 0,
    top: 0
    },
    incomeBox: {
    top: 116
    },
    familyBox: {
    top: 44
    },
    hobbiesBox: {
    top: 92
    },
    friendBox: {
    top: 68
    },
    healthBox: {
    top: 20
    },
    heaBarIcon: {
    top: 21,
    width: 66
    },
    hobBarIcon1: {
    top: 93,
    width: 39
    },
    incBarIcon: {
    top: 117,
    width: 71
    },
    famBarIcon1: {
    top: 45,
    width: 15
    },
    friBarIcon: {
    top: 69,
    width: 60
    },
    family: {
    top: 46,
    width: 33,
    },
    health: {
    top: 23,
    width: 33
    },
    friendship: {
    top: 70,
    width: 42
    },
    hobbies: {
    top: 94,
    width: 33
    },
    income: {
    top: 118,
    width: 65
    },
    stats: {
    left: 154,
    top: 31,
    width: 99
    },
    backgroundParent: {
    flex: 1,
    width: "100%",
    height: 461
    }
});
