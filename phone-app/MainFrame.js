
import * as React from "react";
import {StyleSheet, View} from "react-native";

const MainFrame = () => {
    return (
        <View style={styles.mainFrame} />);
};

const styles = StyleSheet.create({
    mainFrame: {
    borderRadius: 13,
    backgroundColor: "#712aa0",
    shadowColor: "rgba(0, 0, 0, 0.25)",
    shadowOffset: {
    width: 0,
    height: 4
    },
    shadowRadius: 4,
    elevation: 4,
    shadowOpacity: 1,
    borderStyle: "solid",
    borderColor: "#712aa0",
    borderWidth: 1,
    flex: 1,
    width: "100%",
    height: 435
    }
});
export default MainFrame;
    